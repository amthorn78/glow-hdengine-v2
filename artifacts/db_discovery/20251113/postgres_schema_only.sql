--
-- PostgreSQL database dump
--

\restrict XYeiP13agvlvvtNrgqJqPZgqm7IXHFJJGGhVhwqjPhN5SFNaiPviHY3Oevm6hf6

-- Dumped from database version 17.6 (Debian 17.6-2.pgdg13+1)
-- Dumped by pg_dump version 17.7 (Ubuntu 17.7-3.pgdg24.04+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: hde; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA hde;


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: chart_snapshot; Type: TABLE; Schema: hde; Owner: -
--

CREATE TABLE hde.chart_snapshot (
    id uuid NOT NULL,
    user_id text NOT NULL,
    release_id text NOT NULL,
    chart_json jsonb NOT NULL,
    provider text NOT NULL,
    fingerprint text NOT NULL,
    computed_at timestamp with time zone DEFAULT now() NOT NULL,
    CONSTRAINT chart_snapshot_fingerprint_check CHECK ((fingerprint ~ '^[0-9a-f]{64}$'::text)),
    CONSTRAINT chart_snapshot_release_id_check CHECK ((release_id ~ '^[0-9a-f]{64}$'::text))
);


--
-- Name: meta; Type: TABLE; Schema: hde; Owner: -
--

CREATE TABLE hde.meta (
    id text NOT NULL,
    engine_tag text NOT NULL,
    build_commit text NOT NULL,
    invocation_tag text NOT NULL,
    emitter_sha256 text NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    CONSTRAINT meta_emitter_sha256_check CHECK ((emitter_sha256 ~ '^[0-9a-f]{64}$'::text)),
    CONSTRAINT meta_id_check CHECK ((id = 'singleton'::text)),
    CONSTRAINT meta_invocation_tag_check CHECK ((invocation_tag ~ '^INV-[0-9A-Fa-f]+$'::text))
);


--
-- Name: pair_evaluation; Type: TABLE; Schema: hde; Owner: -
--

CREATE TABLE hde.pair_evaluation (
    id uuid NOT NULL,
    min_user text NOT NULL,
    max_user text NOT NULL,
    release_id text NOT NULL,
    bands_json jsonb NOT NULL,
    internal_json jsonb,
    idempotence_hash text NOT NULL,
    evaluated_at timestamp with time zone DEFAULT now() NOT NULL,
    CONSTRAINT pair_evaluation_idempotence_hash_check CHECK ((idempotence_hash ~ '^[0-9a-f]{64}$'::text)),
    CONSTRAINT pair_evaluation_release_id_check CHECK ((release_id ~ '^[0-9a-f]{64}$'::text))
)
PARTITION BY RANGE (evaluated_at);


--
-- Name: pair_evaluation_pcur; Type: TABLE; Schema: hde; Owner: -
--

CREATE TABLE hde.pair_evaluation_pcur (
    id uuid NOT NULL,
    min_user text NOT NULL,
    max_user text NOT NULL,
    release_id text NOT NULL,
    bands_json jsonb NOT NULL,
    internal_json jsonb,
    idempotence_hash text NOT NULL,
    evaluated_at timestamp with time zone DEFAULT now() NOT NULL,
    CONSTRAINT pair_evaluation_idempotence_hash_check CHECK ((idempotence_hash ~ '^[0-9a-f]{64}$'::text)),
    CONSTRAINT pair_evaluation_release_id_check CHECK ((release_id ~ '^[0-9a-f]{64}$'::text))
);


--
-- Name: public_results; Type: TABLE; Schema: hde; Owner: -
--

CREATE TABLE hde.public_results (
    id uuid NOT NULL,
    release_id text NOT NULL,
    payload jsonb NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    CONSTRAINT public_results_release_id_check CHECK ((release_id ~ '^[0-9a-f]{64}$'::text))
)
PARTITION BY RANGE (created_at);


--
-- Name: public_results_pcur; Type: TABLE; Schema: hde; Owner: -
--

CREATE TABLE hde.public_results_pcur (
    id uuid NOT NULL,
    release_id text NOT NULL,
    payload jsonb NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    CONSTRAINT public_results_release_id_check CHECK ((release_id ~ '^[0-9a-f]{64}$'::text))
);


--
-- Name: admin_action_log; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.admin_action_log (
    id integer NOT NULL,
    admin_user_id integer,
    action character varying(50) NOT NULL,
    target_user_id integer,
    details text,
    "timestamp" timestamp without time zone
);


--
-- Name: admin_action_log_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.admin_action_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: admin_action_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.admin_action_log_id_seq OWNED BY public.admin_action_log.id;


--
-- Name: birth_data; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.birth_data (
    user_id integer NOT NULL,
    birth_date date,
    birth_time time without time zone,
    birth_location character varying(255),
    latitude numeric(10,8),
    longitude numeric(11,8),
    data_consent boolean,
    sharing_consent boolean,
    location_display_name text,
    location_country character varying(100),
    location_state character varying(100),
    location_city character varying(100),
    location_importance numeric(5,4),
    location_osm_id bigint,
    location_osm_type character varying(20),
    timezone character varying(50),
    location_source character varying(20) DEFAULT 'manual'::character varying,
    location_verified boolean DEFAULT false,
    CONSTRAINT birth_time_seconds_zero_chk CHECK (((birth_time IS NULL) OR (date_trunc('minute'::text, (birth_time)::interval) = (birth_time)::interval)))
);


--
-- Name: compatibility_matrix; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.compatibility_matrix (
    user_a_id integer NOT NULL,
    user_b_id integer NOT NULL,
    love_score smallint,
    intimacy_score smallint,
    communication_score smallint,
    friendship_score smallint,
    collaboration_score smallint,
    lifestyle_score smallint,
    decisions_score smallint,
    support_score smallint,
    growth_score smallint,
    space_score smallint,
    overall_score smallint,
    calculated_at timestamp without time zone
);


--
-- Name: email_notifications; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.email_notifications (
    id integer NOT NULL,
    user_id integer,
    email_type character varying(50) NOT NULL,
    recipient_email character varying(255) NOT NULL,
    subject character varying(255),
    sent_at timestamp without time zone,
    delivery_status character varying(20)
);


--
-- Name: email_notifications_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.email_notifications_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: email_notifications_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.email_notifications_id_seq OWNED BY public.email_notifications.id;


--
-- Name: human_design_data; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.human_design_data (
    user_id integer NOT NULL,
    chart_data text,
    energy_type character varying(50),
    strategy character varying(100),
    authority character varying(100),
    profile character varying(20),
    api_response text,
    calculated_at timestamp without time zone
);


--
-- Name: user_preferences; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.user_preferences (
    user_id integer NOT NULL,
    prefs json,
    updated_at timestamp without time zone
);


--
-- Name: user_priorities; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.user_priorities (
    user_id integer NOT NULL,
    love_priority smallint,
    intimacy_priority smallint,
    communication_priority smallint,
    friendship_priority smallint,
    collaboration_priority smallint,
    lifestyle_priority smallint,
    decisions_priority smallint,
    support_priority smallint,
    growth_priority smallint,
    space_priority smallint
);


--
-- Name: user_profiles; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.user_profiles (
    id integer NOT NULL,
    user_id integer NOT NULL,
    first_name character varying(50),
    last_name character varying(50),
    bio text,
    age integer,
    profile_completion integer,
    created_at timestamp without time zone,
    updated_at timestamp without time zone,
    display_name character varying(100),
    avatar_url character varying(500)
);


--
-- Name: user_profiles_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.user_profiles_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: user_profiles_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.user_profiles_id_seq OWNED BY public.user_profiles.id;


--
-- Name: user_resonance_prefs; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.user_resonance_prefs (
    user_id integer NOT NULL,
    version integer NOT NULL,
    weights json NOT NULL,
    facets json,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL
);


--
-- Name: user_resonance_signals_private; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.user_resonance_signals_private (
    user_id integer NOT NULL,
    decision_mode character varying(50) NOT NULL,
    interaction_mode character varying(50) NOT NULL,
    connection_style character varying(50) NOT NULL,
    bridges_count smallint NOT NULL,
    emotion_signal boolean NOT NULL,
    work_energy boolean NOT NULL,
    will_signal boolean NOT NULL,
    expression_signal boolean NOT NULL,
    mind_signal boolean NOT NULL,
    role_pattern character varying(50) NOT NULL,
    tempo_pattern character varying(50),
    identity_openness boolean NOT NULL,
    trajectory_code character varying(20),
    confidence json,
    computed_at timestamp without time zone NOT NULL
);


--
-- Name: user_sessions; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.user_sessions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    session_token character varying(255) NOT NULL,
    created_at timestamp without time zone,
    expires_at timestamp without time zone NOT NULL
);


--
-- Name: user_sessions_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.user_sessions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: user_sessions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.user_sessions_id_seq OWNED BY public.user_sessions.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.users (
    id integer NOT NULL,
    email character varying(120) NOT NULL,
    password_hash character varying(255) NOT NULL,
    status character varying(20),
    created_at timestamp without time zone,
    updated_at timestamp without time zone,
    is_admin boolean DEFAULT false NOT NULL,
    profile_version integer DEFAULT 1 NOT NULL
);


--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: pair_evaluation_pcur; Type: TABLE ATTACH; Schema: hde; Owner: -
--

ALTER TABLE ONLY hde.pair_evaluation ATTACH PARTITION hde.pair_evaluation_pcur FOR VALUES FROM ('2025-10-01 00:00:00+00') TO ('2025-11-01 00:00:00+00');


--
-- Name: public_results_pcur; Type: TABLE ATTACH; Schema: hde; Owner: -
--

ALTER TABLE ONLY hde.public_results ATTACH PARTITION hde.public_results_pcur FOR VALUES FROM ('2025-10-01 00:00:00+00') TO ('2025-11-01 00:00:00+00');


--
-- Name: admin_action_log id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.admin_action_log ALTER COLUMN id SET DEFAULT nextval('public.admin_action_log_id_seq'::regclass);


--
-- Name: email_notifications id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.email_notifications ALTER COLUMN id SET DEFAULT nextval('public.email_notifications_id_seq'::regclass);


--
-- Name: user_profiles id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_profiles ALTER COLUMN id SET DEFAULT nextval('public.user_profiles_id_seq'::regclass);


--
-- Name: user_sessions id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_sessions ALTER COLUMN id SET DEFAULT nextval('public.user_sessions_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Name: chart_snapshot chart_snapshot_pkey; Type: CONSTRAINT; Schema: hde; Owner: -
--

ALTER TABLE ONLY hde.chart_snapshot
    ADD CONSTRAINT chart_snapshot_pkey PRIMARY KEY (id);


--
-- Name: chart_snapshot chart_snapshot_user_id_release_id_key; Type: CONSTRAINT; Schema: hde; Owner: -
--

ALTER TABLE ONLY hde.chart_snapshot
    ADD CONSTRAINT chart_snapshot_user_id_release_id_key UNIQUE (user_id, release_id);


--
-- Name: meta meta_pkey; Type: CONSTRAINT; Schema: hde; Owner: -
--

ALTER TABLE ONLY hde.meta
    ADD CONSTRAINT meta_pkey PRIMARY KEY (id);


--
-- Name: pair_evaluation pair_evaluation_min_user_max_user_release_id_evaluated_at_key; Type: CONSTRAINT; Schema: hde; Owner: -
--

ALTER TABLE ONLY hde.pair_evaluation
    ADD CONSTRAINT pair_evaluation_min_user_max_user_release_id_evaluated_at_key UNIQUE (min_user, max_user, release_id, evaluated_at);


--
-- Name: pair_evaluation_pcur pair_evaluation_pcur_min_user_max_user_release_id_evaluated_key; Type: CONSTRAINT; Schema: hde; Owner: -
--

ALTER TABLE ONLY hde.pair_evaluation_pcur
    ADD CONSTRAINT pair_evaluation_pcur_min_user_max_user_release_id_evaluated_key UNIQUE (min_user, max_user, release_id, evaluated_at);


--
-- Name: pair_evaluation pair_evaluation_pkey; Type: CONSTRAINT; Schema: hde; Owner: -
--

ALTER TABLE ONLY hde.pair_evaluation
    ADD CONSTRAINT pair_evaluation_pkey PRIMARY KEY (id, evaluated_at);


--
-- Name: pair_evaluation_pcur pair_evaluation_pcur_pkey; Type: CONSTRAINT; Schema: hde; Owner: -
--

ALTER TABLE ONLY hde.pair_evaluation_pcur
    ADD CONSTRAINT pair_evaluation_pcur_pkey PRIMARY KEY (id, evaluated_at);


--
-- Name: public_results public_results_pkey; Type: CONSTRAINT; Schema: hde; Owner: -
--

ALTER TABLE ONLY hde.public_results
    ADD CONSTRAINT public_results_pkey PRIMARY KEY (id, created_at);


--
-- Name: public_results_pcur public_results_pcur_pkey; Type: CONSTRAINT; Schema: hde; Owner: -
--

ALTER TABLE ONLY hde.public_results_pcur
    ADD CONSTRAINT public_results_pcur_pkey PRIMARY KEY (id, created_at);


--
-- Name: admin_action_log admin_action_log_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.admin_action_log
    ADD CONSTRAINT admin_action_log_pkey PRIMARY KEY (id);


--
-- Name: birth_data birth_data_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.birth_data
    ADD CONSTRAINT birth_data_pkey PRIMARY KEY (user_id);


--
-- Name: compatibility_matrix compatibility_matrix_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.compatibility_matrix
    ADD CONSTRAINT compatibility_matrix_pkey PRIMARY KEY (user_a_id, user_b_id);


--
-- Name: email_notifications email_notifications_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.email_notifications
    ADD CONSTRAINT email_notifications_pkey PRIMARY KEY (id);


--
-- Name: human_design_data human_design_data_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.human_design_data
    ADD CONSTRAINT human_design_data_pkey PRIMARY KEY (user_id);


--
-- Name: user_preferences user_preferences_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_preferences
    ADD CONSTRAINT user_preferences_pkey PRIMARY KEY (user_id);


--
-- Name: user_priorities user_priorities_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_priorities
    ADD CONSTRAINT user_priorities_pkey PRIMARY KEY (user_id);


--
-- Name: user_profiles user_profiles_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_profiles
    ADD CONSTRAINT user_profiles_pkey PRIMARY KEY (id);


--
-- Name: user_profiles user_profiles_user_id_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_profiles
    ADD CONSTRAINT user_profiles_user_id_key UNIQUE (user_id);


--
-- Name: user_resonance_prefs user_resonance_prefs_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_resonance_prefs
    ADD CONSTRAINT user_resonance_prefs_pkey PRIMARY KEY (user_id);


--
-- Name: user_resonance_signals_private user_resonance_signals_private_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_resonance_signals_private
    ADD CONSTRAINT user_resonance_signals_private_pkey PRIMARY KEY (user_id);


--
-- Name: user_sessions user_sessions_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_sessions
    ADD CONSTRAINT user_sessions_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: idx_pair_eval_evaluated_at; Type: INDEX; Schema: hde; Owner: -
--

CREATE INDEX idx_pair_eval_evaluated_at ON ONLY hde.pair_evaluation USING btree (evaluated_at);


--
-- Name: idx_pair_eval_id; Type: INDEX; Schema: hde; Owner: -
--

CREATE INDEX idx_pair_eval_id ON ONLY hde.pair_evaluation USING btree (id);


--
-- Name: idx_pair_eval_release; Type: INDEX; Schema: hde; Owner: -
--

CREATE INDEX idx_pair_eval_release ON ONLY hde.pair_evaluation USING btree (release_id);


--
-- Name: idx_public_results_created_at; Type: INDEX; Schema: hde; Owner: -
--

CREATE INDEX idx_public_results_created_at ON ONLY hde.public_results USING btree (created_at);


--
-- Name: idx_public_results_id; Type: INDEX; Schema: hde; Owner: -
--

CREATE INDEX idx_public_results_id ON ONLY hde.public_results USING btree (id);


--
-- Name: idx_public_results_release_id; Type: INDEX; Schema: hde; Owner: -
--

CREATE INDEX idx_public_results_release_id ON ONLY hde.public_results USING btree (release_id);


--
-- Name: pair_evaluation_pcur_evaluated_at_idx; Type: INDEX; Schema: hde; Owner: -
--

CREATE INDEX pair_evaluation_pcur_evaluated_at_idx ON hde.pair_evaluation_pcur USING btree (evaluated_at);


--
-- Name: pair_evaluation_pcur_id_idx; Type: INDEX; Schema: hde; Owner: -
--

CREATE INDEX pair_evaluation_pcur_id_idx ON hde.pair_evaluation_pcur USING btree (id);


--
-- Name: pair_evaluation_pcur_release_id_idx; Type: INDEX; Schema: hde; Owner: -
--

CREATE INDEX pair_evaluation_pcur_release_id_idx ON hde.pair_evaluation_pcur USING btree (release_id);


--
-- Name: public_results_pcur_created_at_idx; Type: INDEX; Schema: hde; Owner: -
--

CREATE INDEX public_results_pcur_created_at_idx ON hde.public_results_pcur USING btree (created_at);


--
-- Name: public_results_pcur_id_idx; Type: INDEX; Schema: hde; Owner: -
--

CREATE INDEX public_results_pcur_id_idx ON hde.public_results_pcur USING btree (id);


--
-- Name: public_results_pcur_release_id_idx; Type: INDEX; Schema: hde; Owner: -
--

CREATE INDEX public_results_pcur_release_id_idx ON hde.public_results_pcur USING btree (release_id);


--
-- Name: idx_birth_data_city; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX idx_birth_data_city ON public.birth_data USING btree (location_city);


--
-- Name: idx_birth_data_country; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX idx_birth_data_country ON public.birth_data USING btree (location_country);


--
-- Name: idx_birth_data_source; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX idx_birth_data_source ON public.birth_data USING btree (location_source);


--
-- Name: idx_birth_data_verified; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX idx_birth_data_verified ON public.birth_data USING btree (location_verified);


--
-- Name: ix_user_sessions_session_token; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX ix_user_sessions_session_token ON public.user_sessions USING btree (session_token);


--
-- Name: ix_users_email; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX ix_users_email ON public.users USING btree (email);


--
-- Name: pair_evaluation_pcur_evaluated_at_idx; Type: INDEX ATTACH; Schema: hde; Owner: -
--

ALTER INDEX hde.idx_pair_eval_evaluated_at ATTACH PARTITION hde.pair_evaluation_pcur_evaluated_at_idx;


--
-- Name: pair_evaluation_pcur_id_idx; Type: INDEX ATTACH; Schema: hde; Owner: -
--

ALTER INDEX hde.idx_pair_eval_id ATTACH PARTITION hde.pair_evaluation_pcur_id_idx;


--
-- Name: pair_evaluation_pcur_min_user_max_user_release_id_evaluated_key; Type: INDEX ATTACH; Schema: hde; Owner: -
--

ALTER INDEX hde.pair_evaluation_min_user_max_user_release_id_evaluated_at_key ATTACH PARTITION hde.pair_evaluation_pcur_min_user_max_user_release_id_evaluated_key;


--
-- Name: pair_evaluation_pcur_pkey; Type: INDEX ATTACH; Schema: hde; Owner: -
--

ALTER INDEX hde.pair_evaluation_pkey ATTACH PARTITION hde.pair_evaluation_pcur_pkey;


--
-- Name: pair_evaluation_pcur_release_id_idx; Type: INDEX ATTACH; Schema: hde; Owner: -
--

ALTER INDEX hde.idx_pair_eval_release ATTACH PARTITION hde.pair_evaluation_pcur_release_id_idx;


--
-- Name: public_results_pcur_created_at_idx; Type: INDEX ATTACH; Schema: hde; Owner: -
--

ALTER INDEX hde.idx_public_results_created_at ATTACH PARTITION hde.public_results_pcur_created_at_idx;


--
-- Name: public_results_pcur_id_idx; Type: INDEX ATTACH; Schema: hde; Owner: -
--

ALTER INDEX hde.idx_public_results_id ATTACH PARTITION hde.public_results_pcur_id_idx;


--
-- Name: public_results_pcur_pkey; Type: INDEX ATTACH; Schema: hde; Owner: -
--

ALTER INDEX hde.public_results_pkey ATTACH PARTITION hde.public_results_pcur_pkey;


--
-- Name: public_results_pcur_release_id_idx; Type: INDEX ATTACH; Schema: hde; Owner: -
--

ALTER INDEX hde.idx_public_results_release_id ATTACH PARTITION hde.public_results_pcur_release_id_idx;


--
-- Name: admin_action_log admin_action_log_admin_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.admin_action_log
    ADD CONSTRAINT admin_action_log_admin_user_id_fkey FOREIGN KEY (admin_user_id) REFERENCES public.users(id);


--
-- Name: admin_action_log admin_action_log_target_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.admin_action_log
    ADD CONSTRAINT admin_action_log_target_user_id_fkey FOREIGN KEY (target_user_id) REFERENCES public.users(id);


--
-- Name: birth_data birth_data_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.birth_data
    ADD CONSTRAINT birth_data_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: compatibility_matrix compatibility_matrix_user_a_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.compatibility_matrix
    ADD CONSTRAINT compatibility_matrix_user_a_id_fkey FOREIGN KEY (user_a_id) REFERENCES public.users(id);


--
-- Name: compatibility_matrix compatibility_matrix_user_b_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.compatibility_matrix
    ADD CONSTRAINT compatibility_matrix_user_b_id_fkey FOREIGN KEY (user_b_id) REFERENCES public.users(id);


--
-- Name: email_notifications email_notifications_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.email_notifications
    ADD CONSTRAINT email_notifications_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: human_design_data human_design_data_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.human_design_data
    ADD CONSTRAINT human_design_data_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: user_preferences user_preferences_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_preferences
    ADD CONSTRAINT user_preferences_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: user_priorities user_priorities_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_priorities
    ADD CONSTRAINT user_priorities_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: user_profiles user_profiles_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_profiles
    ADD CONSTRAINT user_profiles_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: user_resonance_prefs user_resonance_prefs_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_resonance_prefs
    ADD CONSTRAINT user_resonance_prefs_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: user_resonance_signals_private user_resonance_signals_private_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_resonance_signals_private
    ADD CONSTRAINT user_resonance_signals_private_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: user_sessions user_sessions_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_sessions
    ADD CONSTRAINT user_sessions_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: SCHEMA hde; Type: ACL; Schema: -; Owner: -
--

GRANT USAGE ON SCHEMA hde TO hde_rw;


--
-- Name: TABLE chart_snapshot; Type: ACL; Schema: hde; Owner: -
--

GRANT SELECT,INSERT ON TABLE hde.chart_snapshot TO hde_rw;


--
-- Name: TABLE meta; Type: ACL; Schema: hde; Owner: -
--

GRANT SELECT ON TABLE hde.meta TO hde_rw;


--
-- Name: TABLE pair_evaluation; Type: ACL; Schema: hde; Owner: -
--

GRANT SELECT,INSERT ON TABLE hde.pair_evaluation TO hde_rw;


--
-- Name: TABLE public_results; Type: ACL; Schema: hde; Owner: -
--

GRANT SELECT,INSERT ON TABLE hde.public_results TO hde_rw;


--
-- PostgreSQL database dump complete
--

\unrestrict XYeiP13agvlvvtNrgqJqPZgqm7IXHFJJGGhVhwqjPhN5SFNaiPviHY3Oevm6hf6

